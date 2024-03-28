# target-appsflyer

`target-appsflyer` is a Singer target for AppsFlyer.


## Installation

- [ ] `Developer TODO:` Update the below as needed to correctly describe the install procedure. For instance, if you do not have a PyPi repo, or if you want users to directly install from your git repo, you can modify this step as appropriate.

```bash
pipx install target-appsflyer
```

## Configuration

### Accepted Config Options

- [ ] `Developer TODO:` Provide a list of config options accepted by the target.

A full list of supported settings and capabilities for this
target is available by running:

```bash
target-appsflyer --about
```

### Configure using environment variables

This Singer target will automatically import any environment variables within the working directory's
`.env` if the `--config=ENV` is provided, such that config values will be considered if a matching
environment variable is set either in the terminal context or in the `.env` file.

### Source Authentication and Authorization


```bash
{
  "authorization":"sdk-key"
}
```


### Executing the Target Directly

```bash
target-appsflyer --version
target-appsflyer --help
# Test using the "Carbon Intensity" sample:
tap-carbon-intensity | target-appsflyer --config /path/to/target-appsflyer-config.json
```

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `target_appsflyer/tests` subfolder and
  then run:

```bash
poetry run pytest
```

You can also test the `target-appsflyer` CLI interface directly using `poetry run`:

```bash
poetry run target-appsflyer --help
```

