<template>
  <v-row justify="center">
    <v-btn color="primary" dark @click.stop="dialog = true">
      Acheter Plus
    </v-btn>

    <v-dialog v-model="dialog" transition="slide-x-reverse-transition">
      <v-card>
        <v-card-title class="headline">{{ currency.name }}</v-card-title>

        <v-card-text>
          Let Google help apps determine location. This means sending anonymous
          location data to Google, even when no apps are running.
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn color="green darken-1" text @click="dialog = false">
            Disagree
          </v-btn>

          <v-btn color="green darken-1" text @click="dialog = false">
            Agree
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>
<script>
export default {
  name: 'BuyingButton',
  props: {
    currency: Object,
  },
  data: function() {
    return {
      dialog: false,
    }
  },
}
</script>

<style scoped></style>
