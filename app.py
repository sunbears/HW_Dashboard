# import necessary libraries
from flask import Flask, render_template, jsonify, request, redirect
import pandas as pd

# Flask Setup
app = Flask(__name__)

# Read in CSV using Pandas
metadata_df = pd.read_csv('Belly_Button_Biodiversity_Metadata.csv')
otu_df = pd.read_csv('belly_button_biodiversity_otu_id.csv')
samples_df = pd.read_csv('belly_button_biodiversity_samples.csv')


# Routes

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/names")
def sample_list():
    samples_list = list(samples_df)
    samples_list = samples_list[1:]
    return samples_list


@app.route("/pie")
def pie():
    samples_df = pd.read_csv('belly_button_biodiversity_samples.csv')
    samples_df = samples_df[['otu_id','BB_940']].sort_values('BB_940', ascending=0).head(10)
    samples_df.rename(columns={'BB_940': 'sample_values'}, inplace=True)
    otu_id = samples_df['otu_id'].tolist()
    sample_values = samples_df['sample_values'].tolist()
    data = [{
        "labels": otu_id,
        "values": sample_values,
        "type": "pie"
    }]
    return jsonify(data)

@app.route('/otu')
#Returns a list of OTU descriptions in the following format
def otu_list():
    otu_list = otu_df['lowest_taxonomic_unit_found'].tolist()
    return otu_list


@app.route('/metadata/<sample>')
#sample variable takes the format of 'BB_xxx' so need to convert to number format
def filter_metadata(sample):
    sample_num = int(sample.replace('BB_','')) # strip the string just to the number
    metadata_filtered = metadata_df.loc[metadata_df['SAMPLEID']==sample_num]
    metadata_filtered = metadata_filtered[['AGE','BBTYPE','ETHNICITY','GENDER','LOCATION','SAMPLEID']]
    metadata_filtered = metadata_filtered.to_dict('records')
    metadata_filtered = metadata_filtered[0]
    return metadata_filtered

@app.route('/wfreq/<sample>')
def wfreq_function(sample):
    #sample variable takes the format of 'BB_xxx' so need to convert to number format
    sample_num = int(sample.replace('BB_',''))
    metadata_filtered = metadata_df.loc[metadata_df['SAMPLEID']==sample_num]
    wfreq = metadata_filtered.iloc[0]['WFREQ']
    return int(wfreq)


if __name__ == "__main__":
    app.run()