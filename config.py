from flask import Flask, request , jsonify
import psycopg2
import psycopg2.extras

hostname = 'localhost'
database = 'arkatiss_llp'
owner = 'postgres'
username = 'postgres'
password = 'Jjsb@123'
port_id = 5432
