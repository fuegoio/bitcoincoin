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
      <v-navigation-drawer app clipped permanent width="330" floating>
        <v-list shaped>
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
      </v-navigation-drawer>

      <v-app-bar app color="transparent" flat height="128" clipped-left>
        <v-toolbar-title>
          <img
            src="./assets/logo.png"
            alt="logo"
            class="mb-2"
            style="height: 38px; display: block"
            @click="$router.push('/')"
          />
        </v-toolbar-title>
        <v-row class="ml-2">
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
              flat
              hide-no-data
              hide-details
              label="Quack ! Tu veux trouver une nouvelle crypto ?"
              solo-inverted
            >
            </v-autocomplete>
          </v-col>
          <v-col cols="1">
            <v-btn icon class="mx-3">
              <v-icon>mdi-tag-plus</v-icon>
            </v-btn>
          </v-col>
          <v-col cols="3">
            <v-menu
              v-model="profile"
              :close-on-content-click="false"
              :nudge-width="200"
              offset-x
            >
              <template v-slot:activator="{ on }">
                <v-card flat color="transparent" max-height="48" v-on="on">
                  <v-list color="transparent" class="py-0">
                    <v-list-item>
                      <v-list-item-content class="text-right py-2">
                        <v-list-item-title class="font-weight-bold"
                          >Quentin Churet
                        </v-list-item-title>
                        <v-list-item-subtitle class="caption">
                          Trader
                        </v-list-item-subtitle>
                      </v-list-item-content>

                      <v-list-item-action class="my-0">
                        <v-btn icon disabled>
                          <v-icon>mdi-menu-down</v-icon>
                        </v-btn>
                      </v-list-item-action>
                    </v-list-item>
                  </v-list>
                </v-card>
              </template>

              <v-card>
                <v-list>
                  <v-list-item>
                    <v-list-item-avatar>
                      <img
                        src="https://cdn.vuetifyjs.com/images/john.jpg"
                        alt="John"
                      />
                    </v-list-item-avatar>

                    <v-list-item-content>
                      <v-list-item-title>Quentin Churet</v-list-item-title>
                      <v-list-item-subtitle>
                        Trader
                      </v-list-item-subtitle>
                    </v-list-item-content>
                  </v-list-item>
                </v-list>

                <v-divider />

                <v-list>
                  <v-list-item>
                    <v-list-item-action>
                      <v-switch color="secondary" />
                    </v-list-item-action>
                    <v-list-item-title>Enable notifications</v-list-item-title>
                  </v-list-item>

                  <v-list-item>
                    <v-list-item-action>
                      <v-switch color="secondary" />
                    </v-list-item-action>
                    <v-list-item-title>Enable hints</v-list-item-title>
                  </v-list-item>
                </v-list>

                <v-card-actions>
                  <v-btn color="error" text @click="logout">Deconnexion</v-btn>
                  <v-spacer />
                  <v-btn color="primary" text @click="goProfile">Profile</v-btn>
                </v-card-actions>
              </v-card>
            </v-menu>
          </v-col>
        </v-row>
      </v-app-bar>

      <v-content>
        <v-container fluid>
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
    auth.checkAuth().then(() => {
      this.auth.loading = false
    })
  },
  methods: {
    goProfile(): void {
      this.profile = false
      this.$router.push('/profile')
    },
    logout(): void {
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
}

.theme--dark.v-navigation-drawer {
  background-color: #343949 !important;
}

.theme--dark.v-list {
  background-color: #2a2e3a !important;
}

.v-navigation-drawer .v-list {
  background: #343949 !important;
}
</style>
