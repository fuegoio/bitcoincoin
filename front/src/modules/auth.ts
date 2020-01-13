import axios from 'axios'
import router from '../router'

const user = {
  authenticated: false,
  profile: undefined,
}

function logout(): void {
  localStorage.removeItem('access_token')
  localStorage.removeItem('profile')
  axios.defaults.headers.common['Authorization'] = ''
  user.authenticated = false
  user.profile = null
  router.push('/').catch(err => {})
}

function checkAuth(): Promise<void> {
  return new Promise(resolve => {
    const jwt = localStorage.getItem('access_token')
    if (jwt !== null) {
      axios.defaults.headers.common['Authorization'] = 'Bearer ' + jwt
      axios
        .get('http://localhost:8000/auth/me')
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
      resolve()
    }
  })
}

function login(email: string, password: string) {
  return new Promise((resolve, reject) => {
    axios
      .post('http://localhost:8000/auth/login', {
        email: email,
        password: password,
      })
      .then(response => {
        localStorage.setItem('access_token', response.data.access_token)
        checkAuth().then(() => {
          resolve()
        })
      })
      .catch(error => {
        reject(error.response.data.msg)
      })
  })
}

export default {
  user,
  login,
  checkAuth,
  logout,
}
