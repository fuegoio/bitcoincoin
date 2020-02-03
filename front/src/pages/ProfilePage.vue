<template>
  <v-row class="fill-height">
    <v-col cols="12">
      <ProfileCard :profile="user" />
    </v-col>
    <v-col cols="12" class="my-2">
      <WalletContainer />
    </v-col>
    <v-col cols="12" class="my-2">
      <ProfileTransactions :transactions="transactions" />
    </v-col>
  </v-row>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'

import ProfileCard from '@/components/profiles/ProfileCard.vue'
import WalletContainer from '@/containers/WalletContainer.vue'
import ProfileTransactions from '@/components/profiles/ProfileTransactions.vue'

import auth from '../modules/auth'
import { Transaction } from '@/models/transaction'
import axios, { AxiosResponse } from 'axios'

@Component({
  components: {
    WalletContainer,
    ProfileCard,
    ProfileTransactions,
  },
})
export default class ProfilePage extends Vue {
  user = auth.user.profile
  transactions: Transaction[] = []

  async fetchProfileTransactions(): Promise<Transaction[]> {
    const response: AxiosResponse = await axios.get('/me/transactions')
    return response.data
  }

  created() {
    this.fetchProfileTransactions().then(transactions => {
      this.transactions = transactions
    })
  }
}
</script>

<style scoped></style>
