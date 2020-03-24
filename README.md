# ccfd-seldon-usertask-model

Seldon model trained with the [Kaggle credit card fraud dataset](https://www.kaggle.com/mlg-ulb/creditcardfraud).

To build the model:

```shell
$ s2i build https://github.com/ruivieira/ccfd-seldon-usertask-model.git seldonio/seldon-core-s2i-python36:0.18 ruivieira/ccfd-seldon-usertask-model
```

Make sure you use version `0.18` of the `s2i` has other versions are known to incur in problems in the resulting image.