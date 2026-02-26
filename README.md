# LAB for PaaS group to get in touch with multi agents development

## Set up

### Poetry set up

To install poetry (with unix/linux)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Then add Poetry to PATH

```bash
export PATH="$HOME/.local/bin:$PATH"
```

**Optional for .zsh** 

Add export command to `~/.zshrc` and then

```bash
source ~/.zshrc
```

Sanity check with

```bash
poetry --version
```

### Kaggle setup

Visit [Kaggle](https://www.kaggle.com/settings), create Legacy API Credential, download `kaggle.json` file then

```bash
mkdir -p ~/.kaggle
mv ~/Downloads/kaggle.json ~/.kaggle/
chmod 700 ~/.kaggle/kaggle.json
```

To download kaggle competition, after joined it on kaggle, run

```bash
poetry run kaggle competitions download -c my-competition
```

### API Keys

A `.env` file must be provided, following the `.env-example`

### Qdrant

To enable local Qdrant run set flag in `.env` file and run container with

```bash
docker run -d \
  --name qdrant \
  --restart unless-stopped \
  -p 6333:6333 \
  -p 6334:6334 \
  -v qdrant_storage:/qdrant/storage \
  -e QDRANT__SERVICE__GRPC_PORT=6334 \
  qdrant/qdrant:latest
```

To run qdrant via API build the cluster and set up keys in `.env` file

### Cohere

Get API keys from [Cohere](https://dashboard.cohere.com/api-keys)

### Dependencies

Dependencies can be installed through

```bash
poetry install
```

## Structure

### Competition

Package to suite code for competition

### Templates

Package to suite useful examples to use during competition

### Utils

Package to suite general utils (e.g. dataset parsing)

## Run

To run scripts using virtual environment built by means of `poetry`, run your script with

```bash
poetry run python src/paas_lab/my-package/my-script.py
```

## Results

Results should be collected in `results` folder, by `timestamp.csv`, then moved to `results-to-keep` saving `timestamp-precision.csv`