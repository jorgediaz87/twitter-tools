<template>
    <b-container>
        <b-button @click="block()" block variant="danger">Block all listed accounts</b-button>
        <b-progress v-if="showProgressBar" :max="max" show-progress animated>
            <b-progress-bar
                :value="value"
                :label="`${((value / max) * 100).toFixed(2)}%`"
            ></b-progress-bar>
        </b-progress>
    </b-container>
</template>

<script>
import axios from 'axios';
const delay = (milisecs) => {
    return new Promise((resolve) => {
        setTimeout(resolve, milisecs);
    });
};

export default {
    name: 'blockAll',
    data() {
        return {
            showProgressBar: false,
            max: null,
            value: null,
        };
    },
    props: {
        profiles: {
            type: Array,
            default: null,
        },
    },
    methods: {
        async block() {
            this.showProgressBar = true;
            this.max = this.profiles.length;
            // https://stackoverflow.com/a/34349073
            for (const [index, profile] of this.profiles.entries()) {
                this.value = index;
                axios
                    .post(`http://localhost:5000/api/1.0/profiles/block/${profile.id}`)
                    .then((res) => {
                        console.log(res);
                    })
                    .catch((error) => {
                        console.error(error);
                    });
                await delay(Math.floor(1500 + Math.random() * (1500 + 1 - 5000)));
            }
            this.showProgressBar = false;
        },
    },
};
</script>

<style></style>
