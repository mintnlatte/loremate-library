# Parser Design

`src/parser.py` 의 인자 파싱 + 계산 + 디스패치 deep-dive. 본 모듈이 전체 동작의 핵심 분기를 담는다.

## 함수 목록

| 함수 | 시그니처 | 책임 |
|---|---|---|
| `parse_args` | `parse_args(argv)` | argparse `Namespace` 반환. positional `n: int`, optional `--seq` flag |
| `_fib` | `_fib(n: int) -> int` | 재귀 피보나치. `@lru_cache(maxsize=None)` 로 메모이즈 |
| `run_command` | `run_command(args)` | `args.seq` 분기로 단일 값 또는 시퀀스 반환 |

## CLI 인자

`src/parser.py:5-9` 정의:

```python
p = argparse.ArgumentParser(prog="fib-tools")
p.add_argument("n", type=int)
p.add_argument("--seq", action="store_true")
```

- `n` — 필수 정수 positional. 단일 모드에선 피보나치 인덱스, `--seq` 모드에선 출력할 시퀀스 길이 (`range(args.n)`)
- `--seq` — flag. 켜면 시퀀스 출력 모드

## 계산 — `_fib`

`src/parser.py:12-16`:

```python
@lru_cache(maxsize=None)
def _fib(n: int) -> int:
    if n < 2:
        return n
    return _fib(n - 1) + _fib(n - 2)
```

클래식 재귀 정의 (`n < 2 → n`, 그 외 `_fib(n-1) + _fib(n-2)`) 에 `@lru_cache(maxsize=None)` 데코레이터를 적용해 모든 호출을 캐시한다. 캐시는 무제한 (`maxsize=None`) 이며 모듈 수명 동안 유지되므로, 같은 인터프리터 내 반복 호출은 O(1) 조회로 응답한다.

## 디스패치 — `run_command`

`src/parser.py:19-22`:

```python
def run_command(args):
    if args.seq:
        return [_fib(i) for i in range(args.n)]
    return _fib(args.n)
```

분기는 `args.seq` truthy 여부 단 하나.

- `args.seq == True` → 길이 `args.n` 리스트, 각 원소 `_fib(i)` for `i in range(args.n)`
- `args.seq == False` → 단일 정수 `_fib(args.n)`

리스트와 스칼라 두 가지 반환 형태가 섞이며, 출력 측 `src/utils.py:format_output` 이 `isinstance(result, list)` 분기로 처리한다 (리스트는 `", "` join, 그 외는 `str()`).

## 호출 경로

`main.py:7-9` 가 본 모듈의 진입을 담당한다.

```python
args = parse_args(sys.argv[1:])
result = run_command(args)
print(format_output(result))
```

파서 모듈 외부에서 직접 호출되는 함수는 `parse_args` 와 `run_command` 둘이며, `_fib` 는 모듈 내부 보조 함수 (`_` 접두사 컨벤션) 이지만 `tests/test_main.py:1` 이 단위 테스트 목적으로 import 하고 있다.
