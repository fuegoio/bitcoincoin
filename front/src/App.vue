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
        v-model="drawer"
        app
        width="360"
        clipped
        class="elevation-4 background"
      >
        <ProfileSummaryCard :profile="auth.user.profile" />

        <v-divider class="mt-8" />

        <v-list rounded class="transparent">
          <v-list-item-group color="primary">
            <v-list-item
              v-for="(item, i) in nav"
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

        <v-btn color="error" text absolute block bottom @click="logout">
          Deconnexion
        </v-btn>
      </v-navigation-drawer>

      <v-app-bar
        app
        class="background elevation-2 px-4"
        height="112"
        clipped-left
      >
        <v-app-bar-nav-icon @click.stop="drawer = !drawer" />

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
            <SearchBar />
          </v-col>
          <v-col cols="2"> </v-col>
          <v-col cols="1">
            <v-btn icon class="mx-3">
              <v-icon>mdi-tag-plus</v-icon>
            </v-btn>
          </v-col>
          <v-col cols="1">
            <v-btn icon class="mx-3">
              <v-icon>mdi-tag-minus</v-icon>
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
import ProfileSummaryCard from '@/components/profiles/ProfileSummaryCard.vue'
import SearchBar from '@/components/SearchBar.vue'

export default Vue.extend({
  name: 'App',
  components: { SearchBar, ProfileSummaryCard, LoginPage },
  data: () => ({
    drawer: true,
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
    nav: [
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

    setInterval(() => auth.checkAuth(undefined), 5000)
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
  margin-left: 16px;
}
</style>
