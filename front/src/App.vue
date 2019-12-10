<template>
  <v-app>
    <v-navigation-drawer app clipped permanent width="290">
      <!-- -->
    </v-navigation-drawer>

    <v-app-bar app color="transparent" flat height="128" clipped-left>
      <v-toolbar-title>
        <img
          src="./assets/logo.png"
          alt="logo"
          style="height: 38px; display: block"
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
        <v-col cols="2"> </v-col>
        <v-col cols="2">
          <v-menu :close-on-content-click="false" :nudge-width="200" offset-x>
            <template v-slot:activator="{ on }">
              <v-card flat color="transparent" v-on="on" max-height="48">
                <v-list color="transparent" class="py-0">
                  <v-list-item>
                    <v-list-item-content class="text-right py-2">
                      <v-list-item-title class="font-weight-bold"
                        >Quentin Churet</v-list-item-title
                      >
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
                    <v-list-item-title>John Leider</v-list-item-title>
                    <v-list-item-subtitle
                      >Founder of Vuetify.js</v-list-item-subtitle
                    >
                  </v-list-item-content>

                  <v-list-item-action>
                    <v-btn icon>
                      <v-icon>mdi-heart</v-icon>
                    </v-btn>
                  </v-list-item-action>
                </v-list-item>
              </v-list>

              <v-divider></v-divider>

              <v-list>
                <v-list-item>
                  <v-list-item-action>
                    <v-switch color="purple"></v-switch>
                  </v-list-item-action>
                  <v-list-item-title>Enable messages</v-list-item-title>
                </v-list-item>

                <v-list-item>
                  <v-list-item-action>
                    <v-switch color="purple"></v-switch>
                  </v-list-item-action>
                  <v-list-item-title>Enable hints</v-list-item-title>
                </v-list-item>
              </v-list>

              <v-card-actions>
                <v-spacer></v-spacer>

                <v-btn text @click="menu = false">Cancel</v-btn>
                <v-btn color="primary" text @click="menu = false">Save</v-btn>
              </v-card-actions>
            </v-card>
          </v-menu>
        </v-col>
      </v-row>
    </v-app-bar>

    <v-content>
      <v-container fluid>
        <router-view></router-view>
      </v-container>
    </v-content>
  </v-app>
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
  name: 'App',
  data: () => ({
    search: {
      query: 'Paracétamol',
      molecule: 0,
      molecules: [
        { name: 'BitCoin', id: 34 },
        { name: 'Ethereum', id: 54 },
        { name: 'CoinCoin', id: 60 },
        { name: 'Bitcoin Cash', id: 70 },
      ],
      loading: false,
    },
  }),
  mounted() {
    if (this.$route.name === 'molecule') {
      this.search.molecule = parseInt(this.$route.params.id)
    }
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
</style>
