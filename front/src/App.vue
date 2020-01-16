<template>
  <v-app>
    <template v-if="auth.loading">
      <v-content class="fill-height">
        <v-container fluid class="fill-height">
          <v-row justify="center" class="fill-height" align="center">
            <v-col class="text-center">
              <v-progress-circular indeterminate />
            </v-col>
          </v-row>
        </v-container>
      </v-content>
    </template>

    <template v-else-if="!auth.user.authenticated">
      <v-content class="fill-height">
        <v-container fluid class="fill-height pa-0">
          <LoginPage />
        </v-container>
      </v-content>
    </template>

    <template v-else>
      <v-navigation-drawer
        app
        width="360"
        clipped
        class="elevation-4 background"
      >
        <v-card outlined class="ma-4" hover to="/profile">
          <v-list-item three-line>
            <v-list-item-content>
              <div class="overline mb-4">Compte</div>
              <v-list-item-title class="headline mb-1">{{
                auth.user.profile.username
              }}</v-list-item-title>
              <v-list-item-subtitle>
                Trader
              </v-list-item-subtitle>
            </v-list-item-content>

            <v-list-item-avatar tile size="80" color="primary">
              <span class="white--text headline">{{
                auth.user.profile.username[0]
              }}</span>
            </v-list-item-avatar>
          </v-list-item>

          <v-card-actions class="py-0 mt-2">
            <v-col>
              Cash
            </v-col>
            <v-col class="text-right">
              {{ auth.user.profile.cash_flow | toCurrency }}
            </v-col>
          </v-card-actions>
          <v-card-actions class="primary py-0">
            <v-col>
              Portfolio
            </v-col>
            <v-col class="text-right font-weight-bold">
              {{ auth.user.profile.wallet_value | toCurrency }}
            </v-col>
          </v-card-actions>
        </v-card>

        <v-list rounded class="mt-4 transparent">
          <v-list-item-group v-model="item" color="primary">
            <v-list-item
              v-for="(item, i) in items"
              :key="i"
              class="pl-10 my-4"
              :to="item.path"
            >
              <v-list-item-icon>
                <v-icon v-text="item.icon" />
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title v-text="item.text" />
              </v-list-item-content>
            </v-list-item>
          </v-list-item-group>
        </v-list>

        <v-btn color="error" text absolute block bottom @click="logout"
          >Deconnexion</v-btn
        >
      </v-navigation-drawer>

      <v-app-bar app class="background elevation-2" height="112" clipped-left>
        <v-toolbar-title>
          <img
            src="./assets/logo.png"
            alt="logo"
            class="mb-2"
            style="height: 38px; display: block"
            @click="$router.push('/')"
          />
        </v-toolbar-title>
        <v-row class="tools">
          <v-col cols="8">
            <v-autocomplete
              v-model="search.molecule"
              :loading="search.loading"
              :items="search.molecules"
              item-text="name"
              item-value="id"
              :search-input.sync="search.query"
              cache-items
              class="mx-4"
              hide-no-data
              hide-details
              placeholder="Quack ! Tu veux trouver une nouvelle crypto ?"
              outlined
              flat
              rounded
            >
            </v-autocomplete>
          </v-col>
          <v-col cols="1">
            <v-btn icon class="mx-3">
              <v-icon>mdi-tag-plus</v-icon>
            </v-btn>
          </v-col>
        </v-row>
      </v-app-bar>

      <v-content class="elevation-4 background darken-1">
        <v-container fluid class="pa-6">
          <v-fade-transition mode="out-in" appear>
            <router-view :key="$route.fullPath" />
          </v-fade-transition>
        </v-container>
      </v-content>
    </template>
  </v-app>
</template>

<script lang="ts">
import Vue from 'vue'
import auth from './modules/auth'

import LoginPage from '@/pages/AuthPage.vue'

export default Vue.extend({
  name: 'App',
  components: { LoginPage },
  data: () => ({
    search: {
      query: '',
      molecule: 0,
      molecules: [
        { name: 'BitCoin', id: 34 },
        { name: 'Ethereum', id: 54 },
        { name: 'CoinCoin', id: 60 },
        { name: 'Bitcoin Cash', id: 70 },
      ],
      loading: false,
    },
    auth: {
      user: auth.user,
      loading: true,
    },
    profile: false,
    item: 0,
    items: [
      { text: 'Dashboard', icon: 'mdi-view-dashboard', path: '/dashboard' },
      { text: 'Monnaies', icon: 'mdi-bitcoin', path: '/currencies' },
      { text: 'Banques', icon: 'mdi-bank', path: '/banks' },
      { text: 'Classement', icon: 'mdi-flag', path: '/ranking' },
    ],
  }),
  created() {
    auth.checkAuth(undefined).then(() => {
      this.auth.loading = false
    })
  },
  methods: {
    goProfile(): void {
      this.profile = false
      this.$router.push('/profile')
    },
    logout(): void {
      this.profile = false
      auth.logout()
    },
  },
})
</script>

<style>
.theme--dark.v-application {
  background: #343949 !important;
}

.theme--dark.v-card {
  background-color: #2a2e3a !important;
  border-radius: 16px !important;
}

.theme--dark.v-list {
  background-color: #2a2e3a !important;
}

.tools {
  margin-left: 80px;
}
</style>
