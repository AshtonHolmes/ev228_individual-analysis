# ev228_individual-analysis
## Overview
This dataset contains reported sightings of zebra mussels (Dreissena polymorpha) across North America. It is not remote sensing or model output; rather, it is a compilation of human observations from many different sources, and each record has a location, a reported date, and a record type, along with other features including comments and other variables that had patchy completion. The data comes from the USGS Nonindigenous Aquatic Species database (https://nas.er.usgs.gov), and I accessed it as a CSV file. Since the sightings come from people and not from a standardized survey, it is important to be careful about what the data communicates.

One thing that stood out right away is how different the record sources are (Figure 1). Database entries make up the largest share at around 4,900 records, followed by personal communication at about 3,000 and journal articles at about 1,200. All the other types combined are only a small portion. This matters because a big part of the dataset depends on people reporting what they saw, so places with more people paying attention could look like they have more mussels.
The second thing I noticed is that sightings are clustered in space and time (Figure 2). Most of the older reports (blue and green) are around the Great Lakes, the Mississippi River, and the eastern half of the country. The newer reports (orange and red) start showing up farther Ist and south in places like Oregon, Oklahoma, and Colorado, which suggests that the mussels have been spreading outward from where they first shoId up.

![image](/Users/shartface/Documents/GitHub/ev228_individual-analysis/specimen-recordtype.png)  
*Figure 1. Number of reported zebra mussel sightings per record type. Database records and personal communication make up most of the dataset.*


![image](/Users/shartface/Documents/GitHub/ev228_individual-analysis/colormap.png)  
*Figure 2. Map of reported zebra mussel sightings colored by reported year (1986–2025). Early sightings are concentrated around the Great Lakes and Mississippi River while more recent sightings appear farther Ist and south.*

## New Analysis
One assumption worth stating is that the number of reported sightings is a good stand in for how many mussels are actually present. I don’t think this is fully true, because reporting effort has probably changed over the years and betIen places.

### Results

Seasonality (Figure 3): Reports are very uneven through the year. They climb from about 130 in April to a peak of roughly 1,780 in August, then stay high in September (about 1,640) and October (about 1,340). February has the fewest at under 50. I think this makes sense because people are on the water more in summer and early fall, so more people have the chance to notice mussels. It might not mean that mussels are actually more common in those months.
Change over time (Figure 4): Sightings start in the late 1980s and jump quickly to a first peak of about 475 in 1991. After that they go up and down, with other high years around 1995, 1999, and 2005 (all about 435–450). From about 2016 on, reports mostly decline, falling to under 100 in some years. The 2025 bar is tiny, but that is probably because the year is incomplete. A decrease in reports could mean fewer new sightings as the spread slows down, or it could mean less reporting effort, and I can’t tell which from this data alone.
Putting it together: The early spike matches the map, where the oldest points are packed together in the Great Lakes region. The newer points are more spread out but there are fewer of them.

![image](/Users/shartface/Documents/GitHub/ev228_individual-analysis/specimen-monthcount.png)  

*Figure 3. Number of reported zebra mussel sightings per month across all years. Reports peak in August and are loIst in winter.*

![image](/Users/shartface/Documents/GitHub/ev228_individual-analysis/specimen-yearcount.png)

*Figure 4. Number of reported zebra mussel sightings per year. Sightings peak in the early 1990s and decline in recent years.*

## Code Index
Coded is in the root directory. Unless otherwise stated, all code is in Python
* `NAS_analysis`: All analysis work on NAC dataset.
  * To replicate the analysis, run `NAS_analysis`.
  * No Gen AI was used in the making of this file.
## Process
For the overall project, I started by loading the zebra mussel data and making some quick plots to see what was actually in it. The record type plot was harder to make than the others because the values were strings like “Journal Article” and “Personal Communication” instead of numbers, so I couldn’t just bin them the way I did with year and month. I had to count each category first and then plot those counts, and the labels were a mess until I flipped it to a horizontal bar chart. In a typical coding session, I would get a rough version of a plot working, then go back and fix the titles, labels, and colors. 
