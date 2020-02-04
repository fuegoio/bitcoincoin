<template>
  <v-row>
    <v-col cols="12">
      <v-card>
        <v-card-title>
          Banques
        </v-card-title>
        <v-data-table :headers="headers" :items="banks" hide-default-footer>
          <template v-slot:item.name="{ item }">
            <v-row align="center" @click="$router.push('/banks/' + item.id)">
              <v-list-item-avatar tile size="18" color="primary">
                <span class="white--text">{{ item.symbol[0] }}</span>
              </v-list-item-avatar>
              <span class="font-weight-bold">
                {{ item.name }}
              </span>
            </v-row>
          </template>
          <template v-slot:item.cash_flow="{ item }">
            <span>{{ item.cash_flow | toCurrency }}</span>
          </template>
          <template v-slot:item.wallet_value="{ item }">
            <span>{{ item.wallet_value | toCurrency }}</span>
          </template>
          <template v-slot:item.value="{ item }">
            <span>{{ item.value | toCurrency }}</span>
          </template>
        </v-data-table>
      </v-card>
    </v-col>
  </v-row>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import axios, { AxiosResponse } from 'axios'
import { Bank } from '@/models/bank'

@Component({})
export default class BanksPage extends Vue {
  banks: Bank[] = []
  headers = [
    { text: 'Nom', value: 'name' },
    { text: 'Symbole', value: 'symbol' },
    { text: 'Cash', value: 'cash_flow' },
    { text: 'Porfolio', value: 'wallet_value' },
  ]

  async fetchBanks(): Promise<Bank[]> {
    const response: AxiosResponse = await axios.get('/banks')
    return response.data
  }

  created(): void {
    this.fetchBanks().then(banks => {
      this.banks = banks
    })
  }
}
</script>

<style scoped></style>
