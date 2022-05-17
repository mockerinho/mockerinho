# Simulation Configuration

Each simulation configuration should be specified in separate file and has YAML or JSON format. For example:

```yaml
request:
  path: /users
  method: POST
  headers:
  - name: Content-Type
    value: application/json
    value_matcher: exact
  body:
    value: '{"name": "Alex"}'
    value_matcher: json

response:
  body: '{ "name": "Alex" }'
  headers:
    - name: Content-Type
      value: application/json
  status: 201
```
