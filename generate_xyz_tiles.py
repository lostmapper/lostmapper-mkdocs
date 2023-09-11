"""Converts a CSV of XYZ tiles into a QGIS qgsXYZTilesConnections file"""

from xml.etree.ElementTree import Element, SubElement, tostring
import mkdocs_gen_files
import csv

connections = Element("qgsXYZTilesConnections", {"version": "1.0"})

with open("docs/xyz-tiles.csv", encoding="utf-8") as csvFile:
    reader = csv.DictReader(csvFile)

    for row in reader:
        entry = SubElement(
            connections,
            "xyztiles",
            {
                "name": row["Name"],
                "url": row["URL"],
                "zmin": row["Min"],
                "zmax": row["Max"],
                "tilePixelRatio": "0",
                "authcfg": "",
                "username": "",
                "password": "",
                "referer": "",
                "http-header:referer": "",
            },
        )

with mkdocs_gen_files.open("qgis-xyz-tiles/xyz-tiles.xml", "wb") as xmlFile:
    xmlFile.write(tostring(connections))
