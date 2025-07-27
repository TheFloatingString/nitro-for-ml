# nitro

A framework to simiplify ML experiments and tracking, inspired by Turbo by Ramp.

```bash
uv sync --reinstall-package local
```

## Examples

Run all experiments:

```bash
uv run nitro --run-all
```

Run specific experiments, based on filepath names relative to project root
directory

```bash
uv run nitro --run-exp "comma-separated experiment names"
```

## Structure

```yaml
<experiment_name>:
  datasets:
    train: List[str] # each str is a filepath to a CSV file
    train_context: List[str]
    test: List[str]  # each str is a filepath to a CSV file
    test_context: List[str]
  preprocessing:     # ordered list of str
  classifier: <str>
  scorer: <str>
```

## Default File Structure

```
/config  # store experiment yaml files
/results # store experiment results here as yaml files
/data    # store CSV files here
```
