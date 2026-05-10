# Architecture

## 모듈 지도

| 모듈 | 책임 | 의존 |
|---|---|---|
| `main.py` | CLI 진입점 — argv 파싱 / 명령 실행 / 출력 | `src/parser.py`, `src/utils.py` |
| `src/parser.py` | argparse 인자 파싱, 피보나치 계산, 명령 디스패치 | stdlib `argparse`, `functools.lru_cache` |
| `src/utils.py` | 결과 포매팅 (스칼라 / 리스트 → 문자열) | (없음 — 순수 stdlib) |

## 의존 흐름

```
main.py ─→ parser.parse_args(sys.argv[1:])
       ─→ parser.run_command(args)
              └─→ parser._fib(...)
       ─→ utils.format_output(result)
       ─→ print(...)
```

`main.py:6` 의 `main()` 은 위 4 단계를 순차 호출하고 `0` 을 반환한다. 모듈은 `if __name__ == "__main__": sys.exit(main())` 로 직접 실행을 처리한다 (`main.py:13-14`).

## 외부 의존성

표준 라이브러리만 사용. `pyproject.toml` / `setup.py` / `requirements.txt` 같은 빌드 메타파일은 존재하지 않는다.

- `argparse` — CLI 인자 파싱 (`src/parser.py:1`)
- `functools.lru_cache` — `_fib` 메모이즈 (`src/parser.py:2`)
- `sys` — `argv` / `exit` (`main.py:1`)

## 테스트

`tests/test_main.py` 에 pytest 스타일 함수 테스트 2 개.

- `test_fib_basic` — `_fib(10) == 55` 검증
- `test_format_list` — `format_output([1, 1, 2]) == "1, 1, 2"` 검증

CI / 빌드 설정 파일은 없다.
