import geopandas as gpd
import sys
import json

def compare_shapefiles(file1, file2):
    gdf1 = gpd.read_file(file1)
    gdf2 = gpd.read_file(file2)

    difference = gdf1.compare(gdf2)

    with open('difference.txt', 'w') as f:
        f.write(str(difference))

if __name__ == "__main__":
    file1 = sys.argv[1]
    file2 = sys.argv[2]

    compare_shapefiles(file1, file2)
