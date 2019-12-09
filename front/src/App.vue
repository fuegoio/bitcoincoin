<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <v-toolbar-title class="font-weight-bold">BitCoinCoin</v-toolbar-title>
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
      ></v-autocomplete>
    </v-app-bar>

    <v-content>
      <v-container fluid class="py-0">
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

<style lang="scss"></style>
