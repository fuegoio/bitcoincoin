<template>
  <v-autocomplete
    v-model="currency"
    :loading="loading"
    :items="currencies"
    item-text="name"
    item-value="id"
    :search-input.sync="query"
    cache-items
    class="mx-4"
    hide-no-data
    hide-details
    placeholder="Quack ! Tu veux trouver une nouvelle crypto ?"
    outlined
    flat
    rounded
    return-object
  >
  </v-autocomplete>
</template>

<script lang="ts">
import { Component, Vue, Watch } from 'vue-property-decorator'
import { Currency } from '@/models/currency'
import axios, { AxiosResponse } from 'axios'

@Component({})
export default class SearchBar extends Vue {
  currency: Currency = null
  currencies: Currency[] = []
  loading = false

  query = ''

  @Watch('query')
  async fetchCurrencies(): Promise<void> {
    const response: AxiosResponse = await axios.get('/currencies', {
      params: { name: this.query },
    })
    this.currencies = response.data
  }
}
</script>

<style scoped>
.currency-icon {
  width: 42px;
  margin-top: 6px;
  margin-right: 22px;
  float: left;
}

.currency-card-name,
.currency-card-value {
  border-bottom: 1px solid #3e3f3e;
}

.currency-card-value {
  border-left: 1px solid #3e3f3e;
}
</style>
