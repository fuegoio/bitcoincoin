<template>
  <v-row>
    <v-col cols="12">
      <v-card v-if="myBanks.length === 0" outlined>
        <v-card-text>
          Vous ne faites partie d'aucune banque, cliquez sur l'une d'entre elle
          pour pouvoir la rejoindre, ou créez en une ci-dessous.
        </v-card-text>
      </v-card>
    </v-col>
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
          <templ1ate v-slot:item.value="{ item }">
            <span>{{ item.value | toCurrency }}</span>
          </templ1ate>
          <template v-slot:item.membership="{ item }">
            <v-icon v-if="item.membership" small color="success">
              mdi-check
            </v-icon>
            <v-icon v-else small color="error">
              mdi-cancel
            </v-icon>
          </template>
        </v-data-table>
      </v-card>
    </v-col>
    <v-col cols="12">
      <v-card outlined>
        <v-card-title>
          Fonder une banque
        </v-card-title>
        <v-card-text>
          <v-row>
            <v-col cols="8">
              <v-text-field
                v-model="newBankName"
                label="Nom de la banque"
                required
              ></v-text-field>
            </v-col>
            <v-col cols="4">
              <v-text-field
                v-model="newBankSymbol"
                label="Symbole de la banque"
                :counter="3"
                required
              ></v-text-field>
            </v-col>
          </v-row>
        </v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn text color="primary" @click="createBank"
            >Créer ma banque</v-btn
          >
        </v-card-actions>
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
  myBanks: Bank[] = []
  headers = [
    { text: 'Nom', value: 'name' },
    { text: 'Symbole', value: 'symbol' },
    { text: 'Cash', value: 'cash_flow' },
    { text: 'Porfolio', value: 'wallet_value' },
    { text: 'Membre', value: 'membership', align: 'right' },
  ]
  newBankName = ''
  newBankSymbol = ''

  async fetchBanks(): Promise<Bank[]> {
    const response: AxiosResponse = await axios.get('/banks')
    return response.data
  }

  async fetchMyBanks(): Promise<Bank[]> {
    const response: AxiosResponse = await axios.get('/me/banks')
    return response.data
  }

  async createBank(): Promise<void> {
    const response: AxiosResponse = await axios.post('/banks', {
      name: this.newBankName,
      symbol: this.newBankSymbol,
    })
    const data = await response.data
    await this.$router.push('/banks/' + data.id)
  }

  created(): void {
    this.fetchBanks().then(banks => {
      this.fetchMyBanks().then(myBanks => {
        this.myBanks = myBanks
        banks.forEach(bank => {
          if (this.myBanks.find(b => b.id === bank.id)) {
            bank.membership = true
          }
        })
        this.banks = banks
      })
    })
  }
}
</script>

<style scoped></style>
