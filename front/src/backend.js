import axios from 'axios'

const API_URL = 'https://ip10back.herokuapp.com/';

let $axios = axios.create({
  baseURL: API_URL,
  timeout: 5000,
})

export default {

  registration(data) {
    return $axios.post(`register`, data)
      .then(response => response.data)
  },
  graphicBattle(data) {
    return $axios.post(`graphic_battle`, data)
      .then(response => response.data)
  },

  feedback (data) {
    return $axios.post(`feedback`, data)
      .then(response => response.data)
  },
}
