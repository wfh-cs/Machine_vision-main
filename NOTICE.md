# Third-party notice and release checklist

## Third-party source

`ultralytics/` is vendored third-party source. Its `__init__.py` identifies the upstream project as Ultralytics 8.4.13 under AGPL-3.0. Preserve its copyright and license materials when redistributing this repository.

## Model artifacts

`best.pt`, `best.onnx`, `newb.pt`, and `gear.dlc` are model artifacts. Their training data, provenance, and redistribution rights are not documented in this repository. Confirm that they may be published before making the GitHub repository public.

## Before release

1. Confirm rights for all model weights and training data.
2. Decide whether the repository should be public or private.
3. Review the AGPL-3.0 obligations for the vendored Ultralytics source and any intended deployment model.
4. Remove local serial-port details or sample production data if they are sensitive.
