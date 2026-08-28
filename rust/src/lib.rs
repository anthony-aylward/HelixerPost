use pyo3::prelude::*;
use pyo3::exceptions::PyTypeError;

pub mod analysis;
pub mod gff;
pub mod results;

#[pymodule]
fn helixer_post_bin(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    Ok(())
}