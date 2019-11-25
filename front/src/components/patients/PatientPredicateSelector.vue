<template>
  <div class="d-flex">
    <v-menu open-on-hover>
      <template v-slot:activator="{ on }">
        <v-btn :class="{ accent: !!selectedItem }" v-on="on">
          {{ !!selectedItem ? selectedItem[itemValue] : label }}
        </v-btn>
      </template>
      <v-list>
        <v-list-item
          v-for="item in items"
          :key="item[itemValue]"
          @click="onItemSelected(item)"
        >
          {{ item[itemLabel] }}
        </v-list-item>
      </v-list>
    </v-menu>
    <v-icon v-if="!!selectedItem" @click="onItemSelected(null)">
      mdi-close
    </v-icon>
  </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'

@Component({})
export default class PatientPredicateSelector extends Vue {
  @Prop({ required: true }) public label!: string
  @Prop({ required: true }) public items!: object[]
  @Prop({ required: true }) public itemValue!: string
  @Prop({ required: true }) public itemLabel!: string

  public selectedItem: object | null = null

  public onItemSelected(item: object): void {
    this.$emit('change', item)
    this.selectedItem = item
  }
}
</script>

<style lang="scss" scoped></style>
