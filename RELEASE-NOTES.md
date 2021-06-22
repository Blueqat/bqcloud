# 0.0.6 - 2021-06-22
## Destructive changes
- Arguments `group` and `send_email` of `Api.execute()` are removed.
    - Use `option`. Refer "New features" section.
- `Device.Aspen8` is removed because it's retired.

## New features
- `Api.execute()` has `option` argument.
    - The type of `option` is a dictionary.
    - For cloud task, you can use `{ 'group': str, 'send_email': bool }`.
    - For local task, you can use `{ 'backend': str, 'run_option': {...} }`.
- Add new devices, `SimSv1`, `SimTn1`, `SimDm1`.

## Deprecated
- `Api.save_api` is deprecated. Use `Api.save_to_file`.
