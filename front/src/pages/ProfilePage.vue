<template>
  <v-row class="fill-height">
    <v-col cols="12">
      <ProfileCard :profile="user" />
    </v-col>
    <v-col cols="12" class="my-2">
      <WalletContainer />
    </v-col>
  </v-row>
</template>

<script>
import { Component, Vue } from 'vue-property-decorator'

import ProfileCard from '@/components/profiles/ProfileCard'
import WalletContainer from '@/containers/WalletContainer'

import auth from '../modules/auth'

@Component({
  components: {
    WalletContainer,
    ProfileCard,
  },
})
export default class ProfilePage extends Vue {
  user = auth.user.profile
}
</script>

<style scoped></style>
