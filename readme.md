#### Preprocessor

``` yaml
pass-thru:
  - model-deduplicator
  - subset-reducer

use-extension:
  "@autorest/modelerfour": "4.22.3"

pipeline:

# --- extension remodeler ---

  # "Shake the tree", and normalize the model
  modelerfour:
    input: openapi-document/multi-api/identity     # the plugin where we get inputs from
    additional-checks: true
    naming:
      preserve-uppercase-max-length: 2
  
  # allow developer to do transformations on the code model.
  modelerfour/new-transform:
    input: modelerfour

  dummy:
    input: modelerfour/identity
```
