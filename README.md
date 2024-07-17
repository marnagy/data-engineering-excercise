# Tasks' description

## I.

I downloaded files manually from GDrive and email attachment and moved them into project directory.

There was a problem with running the provided script to extract vectors (module `gensim` expected methods in `scipy` that were **deprecated** -> downgrade `scipy`)

## II.

I used simple word processing by reading lines from file instead of `pandas` module since it will be easier to move to processing streaming data (for example when receiving data from Kafka or other MessageQueue service) when compared to using the aforementioned module.

1. This is implemented in method `load_normalized_phrases()` in file `custom_lib.py`
2. Computation of distances is in the end of function `main()` function in script `process.py`.
3. This is implemented in script `any_input.py`.

# III.

I implemented a simple Flask API to process request for closest phrase.

## Possible future improvements

1. use parallel processing to load and process vectors faster (modules: multiprocessing, Dask, Polars, Ray)
2. in process.py, we can exclude half of the final distances matrix. Then we would have to create wrapper class, that handles case "if matrix[i,j] == 0 and i != j then return matrix[j,i]"
3. Make frontend of the app prettier.
4. Implement frontend where instead of returning new page we only modify existing page.

## Docker

Both `Dockerfile` and `docker-compose.yaml` have been created, but due to time constrains were not thoroughly tested. However, I believe the idea of the container should be clear to any developer that worked with Docker.

Since the app was tested locally, Dockerfile uses pip to install modules, but given more time I prefer using poetry since it handles dependencies a bit more carefully using `pyproject.toml` and `poetry.lock` files.

## Other

Since I was not educated on using `setup.py` or `project.toml` before this test, I will have to skip this part of assignment.