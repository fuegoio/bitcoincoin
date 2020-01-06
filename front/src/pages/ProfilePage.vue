<template>
  <v-row class="fill-height">
    <v-col cols="3">
      <ProfileContainer />
    </v-col>
    <v-col cols="9">
      <WalletContainer />
    </v-col>
  </v-row>
</template>

<script>
import ProfileContainer from '@/containers/ProfileContainer'
import WalletContainer from '@/containers/WalletContainer'

export default {
  name: 'ProfilePage',
  components: {
    WalletContainer,
    ProfileContainer,
  },
}
</script>

<style scoped></style>
