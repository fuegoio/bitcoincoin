<template>
  <v-row>
    <v-col v-for="currency in currencies" :key="currency.name" cols="6">
      <CurrencyCard :currency="currency" />
    </v-col>
  </v-row>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import CurrencyCard from '@/components/currencies/CurrencyCard.vue'
import { Currency } from '@/models/currency'
import axios, { AxiosResponse } from 'axios'

@Component({
  components: {
    CurrencyCard,
  },
})
export default class CurrenciesContainer extends Vue {
  currencies: Currency[] = []

  async fetchCurrencies(): Promise<Currency[]> {
    const response: AxiosResponse = await axios.get('/currencies')
    return response.data
  }

  created() {
    this.fetchCurrencies().then(currencies => {
      this.currencies = currencies
    })
  }
}
</script>

<style scoped></style>
