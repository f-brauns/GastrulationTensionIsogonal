# GastrulationTensionIsogonal
Code for the eLife paper "The Geometric Basis of Epithelial Convergent Extension" https://doi.org/10.7554/eLife.95521


## Repository structure

**/Code/WT**

pre-processing.nb
- load from Stern et al. files
- def of regions
- lagrangian coordinate frames (App. 1\[Dash]Fig. 1)

tectonics.nb
- rearrangement events: interface collapses and creations
- orientation of interface losses (Fig. 1S2)
- T1s vs rosettes (Fig. 1E,E')

T1-length-tension-dynamics.nb
- tension and length dynamics (Fig. 2, Fig. 2S1)
- tension vs time-to-collapse correlation (Fig. 2J,H, Fig. 2S2)

T1-quartet-analysis.nb
- find cell quartets that undergo T1s
- tesion-isogonal decomposition for cell quartets (Fig. 4, Fig. 4S1)

tissue-scale-analysis.nb
- tension anisotropy
- isogonal strain (Fig. 6, Fig. 6S1)
- LTC (Fig. 8, 8S1, 8S2)

AP-stripes.nb
- stripe pattern preservation (Fig. 1S3)

**/Code/Snail**

T1-length-tension-dynamics.nb
- tension inference (Fig. 7)

tissue-scale-analysis.nb
- isogonal strain (Fig. 7S1)
- LTC (Fig. 8)


**/Data**
  - /WT
  - /Snail


## Data source

Cell segmentation and tracking data for the WT embryo from Stern et al. Current Biology (2022) [https://doi.org/10.1016/j.cub.2022.02.059] deposited on figshare [https://doi.org/10.6084/m9.figshare.18551420.v3]. Download the "Data analysis.zip" archive and unpack it. Move the content of the directory "/Data Analysis/Deconstructing Gastrulation - Data/Img_1620 (intercalations)/Mesh/" into the "Data/WT/" directory of this repository. 

## General notes
- The suffix TS in symbol ("variable") names indicates time series
