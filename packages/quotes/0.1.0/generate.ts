import * as path from "https://deno.land/std@0.57.0/path/mod.ts";
import yaml from "https://esm.sh/yaml@2.1.3";

type Package = { matches: Array<{ trigger: string; replace: string }> };

const dirPath = path.dirname(path.fromFileUrl(import.meta.url));
const data = await Deno.readTextFile(path.join(dirPath, "package.yml"));
const parsedData = yaml.parse(data) as Package;
const comments = [...(data.matchAll(/^\s*#\s*(.+)$/gm) ?? [])].map((
  [_match, group],
) => group);
let result = "";

for (let i = 0; i < comments.length; i++) {
  const comment = comments[i];
  const { trigger, replace } = parsedData.matches[i];
  result += `| ${trigger} | ${replace} | ${comment}\n`;
}

const template = await Deno.readTextFile(
  path.join(dirPath, "README-template.md"),
);
const readmePath = path.join(dirPath, "README.md");
await Deno.writeTextFile(
  path.join(dirPath, "README.md"),
  template.replace("%usage%", result),
);

console.log(`Wrote ${readmePath}.`);
