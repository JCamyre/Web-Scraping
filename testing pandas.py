import pandas as pd 
list1 = [['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'],
['NOW', 'ZM', 'FTAI', 'CEVA', 'KGC', 'UBER', 'DSM', 'NSA', 'HPP', 'ERIC', 'GOODP', 'GOODO', 'GOODM', 'GOOD', 'EHTH', 'TROX', 'CSII', 'MTRX', 'CRSAU', 'BECN'],
['ServiceNow, Inc.', 'Zoom Video Communications, Inc.', 'Fortress Transportation and Infrastructure Investors LLC', 'CEVA, Inc.', 'Kinross Gold Corporation', 'Uber Technologies, Inc.', 'BNY Mellon Strategic Municipal Bond Fund, Inc.', 'National Storage Affiliates Trust', 'Hudson Pacific Properties, Inc.', 'Telefonaktiebolaget LM Ericsson (publ)', 'Gladstone Commercial Corporation', 'Gladstone Commercial Corporation', 'Gladstone Commercial Corporation', 'Gladstone Commercial Corporation', 'eHealth, Inc.', 'Tronox Holdings plc', 'Cardiovascular Systems, Inc.', 'Matrix Service Company', 'Crescent Acquisition Corp.', 'Beacon Roofing Supply, Inc.'],
['Technology', 'Technology', 'Services', 'Technology', 'Basic Materials', 'Technology', 'Financial', 'Financial', 'Financial', 'Technology', 'Financial', 'Financial', 'Financial', 'Financial', 'Financial', 'Basic Materials', 'Healthcare', 'Basic Materials', 'Conglomerates', 'Industrial Goods'],
['Information Technology Services', 'Application Software', 'Rental & Leasing Services', 'Semiconductor - Specialized', 'Gold', 'Application Software', 'Closed-End Fund - Debt', 'REIT - Industrial', 'REIT - Office', 'Communication Equipment', 'REIT - Diversified', 'REIT - Diversified', 'REIT - Diversified', 'REIT - Diversified', 'Insurance Brokers', 'Chemicals - Major Diversified', 'Medical Appliances & Equipment', 'Oil & Gas Equipment & Services', 'Conglomerates', 'General Building Materials'],
['USA', 'USA', 'USA', 'USA', 'Canada', 'USA', 'USA', 'USA', 'USA', 'Sweden', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA'],
['50.44B', '26.06B', '1.24B', '679.66M', '6.32B', '69.44B', '418.65M', '1.83B', '5.19B', '30.13B', '792.96M', '789.91M', '743.53M', '687.98M', '2.50B', '1.41B', '1.66B', '509.14M', '503.26M', '2.02B'],
['17588.00', '7850.00', '7625.00', '2764.55', '2525.00', '2225.00', '2120.00', '1606.00', '1533.64', '1441.67', '1243.42', '1238.64', '1165.91', '963.04', '958.86', '956.67', '869.81', '810.87', '779.23', '775.53'],
['263.82', '94.20', '15.25', '30.41', '5.05', '40.05', '8.48', '32.12', '33.74', '8.65', '27.36', '27.25', '25.65', '22.15', '109.31', '8.61', '46.97', '18.65', '10.13', '29.47'],
['-1.23%', '-1.64%', '-0.52%', '-3.15%', '-1.75%', '-6.80%', '0.12%', '1.26%', '-2.37%', '-0.80%', '1.17%', '0.18%', '0.58%', '0.36%', '-0.92%', '-4.44%', '-0.04%', '0.54%', '0.00%', '2.43%'],
['898,414', '801,923', '54,815', '170,715', '13,497,050', '35,016,112', '111,673', '502,427', '3,334,043', '3,367,616', '5,138', '91', '710', '85,856', '209,320', '1,652,603', '305,128', '139,584', '64', '994,248']]
df = pd.DataFrame(list1, columns=[x for x in range(20)])

print(df)
# I have to do one list has an entire company
