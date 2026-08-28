use pyo3::prelude::*;
// use pyo3::exceptions::PyTypeError;

pub mod analysis;
pub mod gff;
pub mod results;

#[pymodule]
mod helixer_post_bin {
    use pyo3::prelude::*;
}
