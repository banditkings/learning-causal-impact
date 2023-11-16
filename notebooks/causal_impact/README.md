## Causal Impact

Comparison of different libraries for measuring causal impact (i.e. from the `CausalImpact` R library) in Python. `CausalImpact` has various translations in Python 

## `CausalPy` vs `CausalImpact`

`CausalPy` supported by PyMC labs, whereas the `CausalImpact` library from Google is in R with translations to python in `pyCausalImpact` and `tfcausalimpact`. 

Both `CausalPy` and `CausalImpact` offer similar functionality, but `CausalPy` allows for both `sklearn` and `pymc` (regression-based) models and they are continuing to expand. At this time, `CausalPy` doesn't use the BSTS model as seen in the original `CausalImpact` lirary. 

### Regression vs BSTS

I also tried out `sts-jax` but the documentation was outdated and it looks like development has stopped. It took a little work to get it to work and when it did, it was still slow. It might be good for structural time series but haven't tried it - especially considering `pymc-experimental` added their own rendition of structural time series and `sts-jax` hasn't been touched in a while. 

`tfcausalimpact` seems to be the most stable out of the bunch if we want something close to the R version and use BSTS as the preferred model.