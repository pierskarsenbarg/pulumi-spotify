import * as spotify from "@pulumi/spotify";

const random = new spotify.Random("my-random", { length: 24 });

export const output = random.result;