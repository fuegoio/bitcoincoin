<template>
  <v-row>
    <v-col v-for="currency in currencies" :key="currency.name" cols="12" sm="6">
      <CurrencyCard :currency="currency" />
    </v-col>
    <v-col cols="12" class="text-center my-4">
      <mugen-scroll :handler="addCurrencies" :should-handle="!loading">
        <v-progress-circular indeterminate></v-progress-circular>
      </mugen-scroll>
    </v-col>
  </v-row>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import MugenScroll from 'vue-mugen-scroll'
import CurrencyCard from '@/components/currencies/CurrencyCard.vue'
import { Currency } from '@/models/currency'
import axios, { AxiosResponse } from 'axios'

@Component({
  components: {
    CurrencyCard,
    MugenScroll,
  },
})
export default class CurrenciesContainer extends Vue {
  currencies: Currency[] = []
  loading = false
  offset = 0

  async fetchCurrencies(): Promise<Currency[]> {
    const response: AxiosResponse = await axios.get('/currencies', {
      params: { offset: this.offset },
    })
    return response.data
  }

  addCurrencies(): void {
    this.loading = true
    this.fetchCurrencies().then(currencies => {
      currencies.map(currency => {
        this.currencies.push(currency)
      })
      this.loading = false
      this.offset += 10
    })
  }

  created() {
    this.addCurrencies()
  }
}
</script>

<style scoped></style>
