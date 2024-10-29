import hashlib
from supabase import create_client, Client

#supabase data connection: URL, KEY
SUPABASE_URL = "https://irmvefnbhyhcymfslrvy.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlybXZlZm5iaHloY3ltZnNscnZ5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzAxNjY2NjQsImV4cCI6MjA0NTc0MjY2NH0.4N8E9PhWy954BEp67QwT-qcMaB5T_cNHEy2DzUBcxas"

#Connect to Supabase Client
supabase: Client = create_client (SUPABASE_URL, SUPABASE_KEY)

#Get and save data function
def save_data(e,p):
    #Inser into users model
    enc_pass = hashlib.sha256(p.encode()).hexdigest()
    response = supabase.table('users').insert({"email":e, "password": enc_pass}).execute()
    
    if response.data:
        print(f"User has been save succesfully: {response.data}")
    elif response.error:
        print(f" Error saving user: {response.error}")
       
#Main
email = input("User e-mail:")
passwd = input("User password:")
save_data(email, passwd)
