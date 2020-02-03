<template>
  <v-row class="fill-height">
    <v-col cols="12">
      <ProfileCard :profile="user" />
    </v-col>
    <v-col v-if="historic.length > 0" cols="12">
      <ProfileHistoric :historic="historic" />
    </v-col>
    <v-col v-else cols="12" class="text-center pa-12">
      <v-progress-circular indeterminate />
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
import ProfileHistoric from '@/components/profiles/ProfileHistoric.vue'

@Component({
  components: {
    ProfileHistoric,
    WalletContainer,
    ProfileCard,
    ProfileTransactions,
  },
})
export default class ProfilePage extends Vue {
  user = auth.user.profile
  transactions: Transaction[] = []
  historic: any[] = []

  async fetchProfileHistoric(): Promise<Transaction[]> {
    const response: AxiosResponse = await axios.get('/me/historic')
    return response.data
  }

  async fetchProfileTransactions(): Promise<Transaction[]> {
    const response: AxiosResponse = await axios.get('/me/transactions')
    return response.data
  }

  created() {
    this.fetchProfileTransactions().then(transactions => {
      this.transactions = transactions
    })

    this.fetchProfileHistoric().then(historic => {
      this.historic = historic
    })
  }
}
</script>

<style scoped></style>
