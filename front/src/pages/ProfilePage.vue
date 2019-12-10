<template>
  <v-row>
    <v-col cols="12">
      <ProfileContainer />
    </v-col>
    <v-col cols="12">
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
