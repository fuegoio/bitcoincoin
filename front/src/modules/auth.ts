import axios from 'axios'
import router from '../router'

const user = {
  authenticated: false,
  profile: undefined,
}

function logout() {
  localStorage.removeItem('access_token')
  localStorage.removeItem('profile')
  axios.defaults.headers.common['Authorization'] = ''
  user.authenticated = false
  user.profile = null
  router.replace('/login')
}

function checkAuth() {
  return new Promise((resolve, reject) => {
    const jwt = localStorage.getItem('access_token')
    if (jwt !== null) {
      axios.defaults.headers.common['Authorization'] = 'Bearer ' + jwt
      axios
        .get(process.env.API_URL + '/me')
        .then(function(response) {
          user.authenticated = true
          user.profile = response.data
          localStorage.setItem('profile', JSON.stringify(user.profile))
          resolve()
        })
        .catch(function() {
          logout()
          resolve()
        })
    } else {
      router.replace('/login')
      resolve()
    }
  })
}

export default {
  user,
  checkAuth,
}
