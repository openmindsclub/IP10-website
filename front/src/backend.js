import axios from 'axios'

const API_URL = 'http://127.0.0.1:5000/api';

let $axios = axios.create({
  baseURL: API_URL,
  timeout: 5000,
})

export default {

  registration() {
    return $axios.post(`register`)
      .then(response => response.data)
  },

  feedback () {
    return $axios.post(`feedback`)
      .then(response => response.data)
  },
}
