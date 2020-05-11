# prop-gen-tool
Generates a .txt file of data points for the profile of a propeller that can be imported into Solidworks or similar CAD software to generate a propeller. Its for personal use and doesn't follow any scientific airflow design method

## Usage

```
from blade import Wing

w = Wing(4,15,1)
print(w)
w.build_wing_generic()
w.plot_profile()
w.export_profile_as_txt()

```



