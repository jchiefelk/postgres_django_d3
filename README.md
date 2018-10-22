<h3>Installing and Configuration</h3>

<pre>
virtualenv --python=python3.6.5 myenv
source myenv/bin/activate
pip install -r requirements.txt
</pre>

<h3>Configure your bash or zsh profile</h3>

<pre>
nano ~/.zshrc
</pre>

or 

<pre>
nano ~/.bash_profile
</pre>

<p>Then add the following environmental variables of the file</p>

<pre>
export POSTGRES_DB_NAME="your_database_name"
export POSTGRES_USER="username"
export POSTGRES_PASSWORD="password"
export POSTGRES_HOST="ip address"
export POSTGRES_PORT="port"
</pre>

<h3>Import data</h3>

<pre>
python3 manage.py import_json --filepath /path/to/npt_adwords_20170101_20180627.json
</pre>

<h3>Deploy locally</h3>

<pre>
./manage.py runserver
</pre>

<p>Then visit to view charts rendered by D3.js</p>
<a>http://localhost:8000/</a>

<h3>Query the api for data</h3>
<p>Query data set using query parameters in your terminal or browser</p>

<pre>
curl -X GET http://127.0.0.1:8000/api?date=2018-05-09
</pre>
