# Correction of Metrics for Clustered Binary Data

This work is part of the research performed at the [Wearable Technologies Lab, Imperial College London, UK](https://www.imperial.ac.uk/wearable-technologies).

## Citations

Please cite the following publication when using this toolbox:
```bibtex
@article{Kok2022,
  author={Kok, Xuen Hoong and Imtiaz, Syed Anas and Rodriguez-Villegas, Esther},
  journal={IEEE Transactions on Biomedical Engineering}, 
  title={Assessing the Feasibility of Acoustic Based Seizure Detection}, 
  year={2022},
  volume={69},
  number={7},
  pages={2379-2389},
  doi={10.1109/TBME.2022.3144634}
}
```

## Installation
* Download or clone the repository and add it to your working path

## Usage

* For each cluster, you'll need:
    * n - the number of observations 
    * x - the number of observations with the desired outcome

### Python
 
* Create a list containing all of the data. For example: _T = [[n<sub>1</sub>, x<sub>1</sub>], [n<sub>2</sub>, x<sub>2</sub>], ..., [n<sub>i</sub>, x<sub>i</sub>]]_ 

```python
import cluster_correction as cc

T = [[12,12], [11,11], [10,10], [9,9], [11,10], [10,9], [10,9], [9,8], [9,8], [5,4], [9,7], [7,4], [10,5], [6,3], [10,3], [7,0]]
alpha = 0.05 

ccm, lci, uci = cc.wilson_confidence_intervals(T, alpha)
```

### MATLAB

* Create a Table containing the following two fields/variables
    * _num_sub_unit_
    * _outcome_

```matlab
T = table();
alpha = 0.05

T.num_sub_unit = [12;11;10;9;11;10;10;9;9;5;9;7;10;6;10;7];
T.outcome      = [12;11;10;9;10;9;9;8;8;4;7;4;5;3;3;0];

[CCM, LCI, UCI] = BinaryClusteredWilsonConfidenceInterval(T, alpha)
```

## Issues

For any issues or bug reports please use GitHub Issues


## Contribute

Submit pull requests

## Contact

* Visit our research group website to know more about our work: [Wearable Technologies Lab](https://www.imperial.ac.uk/wearable-technologies)
* Contact me via [e-mail](mailto:x.kok17@imperial.ac.uk)

## License

&copy; Xuen Hoong Kok | 2022 | MIT License [http://opensource.org/licenses/MIT](http://opensource.org/licenses/MIT)

