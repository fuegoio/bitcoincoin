import Vue from 'vue'
import axios from 'axios'

if (process.env.NODE_ENV === 'development') {
  axios.defaults.baseURL = 'http://localhost:8000/api/v1'
} else {
  axios.defaults.baseURL = 'http://bitcoincoin.kernelpanic.io:8000/api/v1'
}

Vue.prototype.$http = axios
