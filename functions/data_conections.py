from sshtunnel import SSHTunnelForwarder
import psycopg2
import pandas as pd
import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv()) # read local .env file

def fetch_data_via_ssh(remote_postgres_host, remote_postgres_port, dbname, query):
    """
    Fetch data from a PostgreSQL database through an SSH tunnel and return it as a pandas DataFrame.
    
    Parameters:
    - remote_postgres_host (str): Hostname or IP address of the remote PostgreSQL server.
    - dbname (str): Name of the database to connect to.
    - query (str): SQL query to execute.
    
    Returns:
    - pandas.DataFrame: DataFrame containing the query results.

    Important: Make sure postgress is started in your local machine and that in the 'postgresql.conf' 
    file listen_addresses is uncommented and equal to '*' so it accepts all connections.
    """
    # SSH and PostgreSQL configuration
    local_bind_address = '127.0.0.1'
    local_bind_port = 5433  # Choose a free port on your local machine
    
    # Setup SSH tunnel
    try:
        tunnel = SSHTunnelForwarder(
            (os.environ['SSH_HOST'], int(os.environ['SSH_PORT'])),
            ssh_username=os.environ['SSH_USERNAME'],
            ssh_private_key=os.environ['SSH_PRIVATE_KEY'],
            remote_bind_address=(remote_postgres_host, remote_postgres_port), #make that the port is private
            local_bind_address=(local_bind_address, local_bind_port)
        )
        tunnel.start()
        
        # print(f"SSH tunnel established. Local port: {tunnel.local_bind_port}")
        
        # Setup the database connection using psycopg2
        conn = psycopg2.connect(
            dbname=dbname,
            user=os.environ['DB_USERNAME'],
            password=os.environ['DB_PASSWORD'],
            host=local_bind_address,  # Connect to the tunnel
            port=tunnel.local_bind_port  # Use the forwarded port
        )
        
        # print("Connected to the database successfully.")
        
        # Fetch data into a pandas DataFrame
        df = pd.read_sql(query, conn)
        
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        # Close the database connection
        if 'conn' in locals() and conn is not None:
            conn.close()
        # Close the SSH tunnel
        if 'tunnel' in locals() and tunnel is not None:
            tunnel.stop()
    return df

