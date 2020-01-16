<template>
  <v-autocomplete
    v-model="currency"
    :loading="loading"
    :items="currencies"
    :search-input.sync="query"
    item-text="name"
    cache-items
    class="mx-4"
    hide-no-data
    hide-details
    placeholder="Quack ! Tu veux trouver une nouvelle crypto ?"
    outlined
    flat
    rounded
    return-object
    @change="selectCurrency"
  >
    <template v-slot:item="{ item, index }">
      <v-list-item-avatar>
        <v-img :src="item.icon" />
      </v-list-item-avatar>
      <v-list-item-content>
        <v-list-item-title>{{ item.name }}</v-list-item-title>
        <v-list-item-subtitle>{{ item.symbol }}</v-list-item-subtitle>
      </v-list-item-content>
      <v-list-item-icon>
        <span class="font-weight-thin">
          {{ item.last_value | toCurrency }}
        </span>
      </v-list-item-icon>
    </template>
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

  selectCurrency(): void {
    this.$router.push('/currencies/' + this.currency.id)
    this.$nextTick(() => {
      this.currency = null
      this.query = ''
    })
  }
}
</script>

<style scoped></style>
