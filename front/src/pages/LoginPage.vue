<template>
  <v-row class="fill-height">
    <v-col cols="6" class="login">
      <v-row class="fill-height px-10" align="center" justify="center">
        <v-col cols="8">
          <v-form ref="form" v-model="valid" lazy-validation>
            <v-text-field
              v-model="email"
              :rules="emailRules"
              label="E-mail"
              required
              light
              outlined
            />

            <v-text-field
              v-model="password"
              :rules="passwordRules"
              label="Password"
              required
              light
              outlined
              type="password"
            />

            <v-btn
              :disabled="!valid"
              color="primary"
              class="mr-4"
              @click="login"
              block
              light
            >
              Log in
            </v-btn>
          </v-form>
        </v-col>
      </v-row>
    </v-col>
    <v-col cols="6">
      <v-row align="center" justify="center" class="fill-height">
        <v-col>
          <img src="../assets/logo.png" class="logo px-10" />
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import auth from '../modules/auth'

@Component({})
export default class LoginPage extends Vue {
  valid = false
  email = ''
  emailRules = [
    (v: string) => !!v || 'E-mail is required',
    (v: string) => /.+@.+\..+/.test(v) || 'E-mail must be valid',
  ]
  password = ''
  passwordRules = [(v: string) => !!v || 'Password is required']

  login() {
    if (this.$refs.form.validate()) {
      auth.login(this.email, this.password)
    }
  }
}
</script>

<style scoped>
.login {
  background: white;
}

.logo {
  width: 100%;
}
</style>
