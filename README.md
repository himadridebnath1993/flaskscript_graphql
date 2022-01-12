# FLASK with GraphQL 

Once download code have to add URL and key on **app/service/graph_ql.py file**

  `transport = AIOHTTPTransport(url="GRAPH_QL_URL", headers={'Content-Type': 'application/json', 'x-hasura-admin-secret': "SECRET_KEY"})`

Now you have to install all the plugins using **./install.sh** command
<br>Run the application using  **./run.sh** command

**Output:** 
 * Serving Flask app "app"
 * Forcing debug mode on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 867-037-447

